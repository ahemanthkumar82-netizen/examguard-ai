import React, { useEffect, useRef, useState } from 'react';
import * as faceapi from 'face-api.js';
import axios from 'axios';
import './ExamPage.css';

const ExamPage = ({ student, sessionId, onLogout }) => {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [cameraStarted, setCameraStarted] = useState(false);
  const [status, setStatus] = useState({ type: 'warn', text: '📷 Click button to start' });
  const [time, setTime] = useState('00:00:00');
  const [cameras, setCameras] = useState([]);
  const [selectedCamera, setSelectedCamera] = useState('');
  const [warnings, setWarnings] = useState(0);
  const [debug, setDebug] = useState('Loading...');

  const streamRef = useRef(null);
  const detectionIntervalRef = useRef(null);
  const noFaceStartRef = useRef(0);
  const lookDownStartRef = useRef(0);
  const gazeWarningCountRef = useRef(0);
  const gazeAwayStartRef = useRef(0);
  const examStartTimeRef = useRef(null);
  const timerIntervalRef = useRef(null);

  useEffect(() => {
    return () => {
      stopCamera();
      if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
      if (detectionIntervalRef.current) clearTimeout(detectionIntervalRef.current);
    };
  }, []);

  const debugLog = (msg) => {
    console.log(msg);
    setDebug(msg);
  };

  const startTimer = () => {
    examStartTimeRef.current = Date.now();
    timerIntervalRef.current = setInterval(() => {
      const elapsed = Math.floor((Date.now() - examStartTimeRef.current) / 1000);
      const hours = Math.floor(elapsed / 3600);
      const minutes = Math.floor((elapsed % 3600) / 60);
      const seconds = elapsed % 60;
      setTime(
        `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`
      );
    }, 1000);
  };

  const loadCameras = async () => {
    debugLog('Loading cameras...');
    try {
      const devices = await navigator.mediaDevices.enumerateDevices();
      const videoDevices = devices.filter((d) => d.kind === 'videoinput');
      debugLog(`Found ${videoDevices.length} cameras`);
      setCameras(videoDevices);
      if (videoDevices.length > 0) {
        setSelectedCamera(videoDevices[0].deviceId);
        startCamera(videoDevices[0].deviceId);
      }
    } catch (error) {
      debugLog('Camera error: ' + error.message);
      redirectToLogin('blocked');
    }
  };

  const startCamera = async (deviceId) => {
    debugLog('Starting camera...');
    try {
      if (streamRef.current) {
        streamRef.current.getTracks().forEach((track) => track.stop());
      }

      const stream = await navigator.mediaDevices.getUserMedia({
        video: {
          deviceId: deviceId ? { exact: deviceId } : undefined,
          width: { ideal: 1280 },
          height: { ideal: 720 },
        },
      });

      streamRef.current = stream;
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.onloadedmetadata = () => {
          debugLog('Video loaded, setting up canvas...');
          if (canvasRef.current && videoRef.current) {
            canvasRef.current.width = videoRef.current.videoWidth;
            canvasRef.current.height = videoRef.current.videoHeight;
            debugLog(`Canvas: ${canvasRef.current.width}x${canvasRef.current.height}`);
            loadFaceAPI();
          }
        };
      }

      stream.getVideoTracks()[0].addEventListener('ended', () => {
        debugLog('Camera stream ended');
        redirectToLogin('blocked');
      });
    } catch (error) {
      debugLog('Start camera error: ' + error.message);
      redirectToLogin('blocked');
    }
  };

  const stopCamera = () => {
    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => track.stop());
    }
  };

  const changeCamera = (deviceId) => {
    if (detectionIntervalRef.current) clearTimeout(detectionIntervalRef.current);
    setSelectedCamera(deviceId);
    startCamera(deviceId);
  };

  const loadFaceAPI = async () => {
    debugLog('Loading face-api.js models...');
    try {
      const MODEL_URL = 'https://justadudewhohacks.github.io/face-api.js/models';
      await Promise.all([
        faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URL),
        faceapi.nets.faceLandmark68TinyNet.loadFromUri(MODEL_URL),
      ]);
      debugLog('Models loaded! Starting detection...');
      setStatus({ type: 'ok', text: '✅ Detection active' });
      detectLoop();
    } catch (error) {
      debugLog('Model load error: ' + error.message);
      setStatus({ type: 'error', text: '❌ Detection failed' });
    }
  };

  const detectLoop = async () => {
    try {
      if (!videoRef.current || !canvasRef.current) return;

      // Optimized detection settings for all body types, genders, and accessories
      const detections = await faceapi
        .detectAllFaces(videoRef.current, new faceapi.TinyFaceDetectorOptions({ 
          inputSize: 224, 
          scoreThreshold: 0.4  // Lower threshold = better detection for glasses, different face shapes
        }))
        .withFaceLandmarks(true);

      const ctx = canvasRef.current.getContext('2d');
      ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);

      debugLog(`Faces detected: ${detections.length}`);

      // Rule 1: Multiple faces
      if (detections.length > 1) {
        debugLog('VIOLATION: Multiple faces!');
        showAlert('👥 Multiple persons detected!');
        setTimeout(() => redirectToLogin('multiple'), 2000);
        return;
      }

      // Rule 2: No face
      if (detections.length === 0) {
        if (noFaceStartRef.current === 0) noFaceStartRef.current = Date.now();
        const elapsed = (Date.now() - noFaceStartRef.current) / 1000;
        debugLog(`No face: ${elapsed.toFixed(1)}s`);
        if (elapsed >= 2) {
          debugLog('VIOLATION: No face >2s!');
          showAlert('👁️ No face detected for >2 seconds!');
          setTimeout(() => redirectToLogin('face'), 2000);
          return;
        }
        setStatus({ type: 'warn', text: `⚠️ No face (${elapsed.toFixed(1)}s)` });
        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 4;
        ctx.strokeRect(10, 10, canvasRef.current.width - 20, canvasRef.current.height - 20);
      } else {
        noFaceStartRef.current = 0;
        const detection = detections[0];
        const box = detection.detection.box;

        // Draw green box that follows the face - no out of box detection
        ctx.strokeStyle = '#4ade80';
        ctx.lineWidth = 3;
        ctx.strokeRect(box.x, box.y, box.width, box.height);

        // Removed out of box detection - box follows user movement
        // Users can move freely within camera view

        const landmarks = detection.landmarks.positions;
        const nose = landmarks[30];
        const chin = landmarks[8];
        const eyeLeft = landmarks[36];
        const eyeRight = landmarks[45];
        const leftEyeCenter = landmarks[39];
        const rightEyeCenter = landmarks[42];
        const eyeY = (eyeLeft.y + eyeRight.y) / 2;

        // Draw trackers
        drawFaceTracker(landmarks, ctx);
        drawEyeTracker(leftEyeCenter, rightEyeCenter, nose, ctx);

        // Rule 3: Eye Gaze Tracking - Check if looking at screen
        const isLookingAtScreen = checkGazeDirection(landmarks, canvasRef.current);
        
        if (!isLookingAtScreen) {
          if (gazeAwayStartRef.current === 0) gazeAwayStartRef.current = Date.now();
          const elapsed = (Date.now() - gazeAwayStartRef.current) / 1000;
          
          if (elapsed >= 2) {
            // Looking away for 2+ seconds
            gazeWarningCountRef.current += 1;
            setWarnings(gazeWarningCountRef.current);
            debugLog(`GAZE WARNING ${gazeWarningCountRef.current}/3: Looking away from screen!`);
            
            if (gazeWarningCountRef.current >= 3) {
              // 3rd warning - redirect
              showAlert('⚠️ Warning 3/3: Looking away from screen! Exam terminated.');
              setTimeout(() => redirectToLogin('gaze_away'), 2000);
              return;
            } else {
              // 1st or 2nd warning
              playSound();
              showAlert(`⚠️ Warning ${gazeWarningCountRef.current}/3: Keep your eyes on the screen!`);
              setStatus({ type: 'warn', text: `⚠️ Warning ${gazeWarningCountRef.current}/3: Eyes off screen` });
              gazeAwayStartRef.current = 0; // Reset timer after warning
            }
          } else {
            setStatus({ type: 'warn', text: `⚠️ Eyes off screen (${elapsed.toFixed(1)}s)` });
          }
        } else {
          gazeAwayStartRef.current = 0;
        }

        // Rule 4: Head turn
        const faceWidth = Math.abs(landmarks[16].x - landmarks[0].x);
        const headTurnThreshold = faceWidth * 0.25;
        const noseToCenterX = Math.abs(nose.x - (landmarks[0].x + landmarks[16].x) / 2);

        if (noseToCenterX > headTurnThreshold) {
          debugLog('VIOLATION: Head turned!');
          showAlert('🔄 Head turned outside camera!');
          setTimeout(() => redirectToLogin('headturn'), 2000);
          return;
        }

        // Rule 5: Looking down
        const lookingDown = nose.y > eyeY + 15 && chin.y > nose.y + 25;

        if (lookingDown) {
          if (lookDownStartRef.current === 0) lookDownStartRef.current = Date.now();
          const elapsed = (Date.now() - lookDownStartRef.current) / 1000;
          debugLog(`Looking down: ${elapsed.toFixed(1)}s`);
          if (elapsed >= 2) {
            debugLog('VIOLATION: Looking down >2s!');
            showAlert('⏱️ Looking down for >2 seconds!');
            setTimeout(() => redirectToLogin('lookdown'), 2000);
            return;
          }
          setStatus({ type: 'warn', text: `⚠️ Looking down (${elapsed.toFixed(1)}s)` });
        } else {
          lookDownStartRef.current = 0;
        }

        // Rule 6: Sleep detection
        const leftEyeHeight = Math.abs(landmarks[41].y - landmarks[37].y);
        const rightEyeHeight = Math.abs(landmarks[47].y - landmarks[43].y);
        const avgEyeHeight = (leftEyeHeight + rightEyeHeight) / 2;

        // Threshold: 2.5 pixels (adjust for sensitivity)
        // Lower value = more sensitive (detects slight eye closure)
        // Higher value = less sensitive (only detects fully closed eyes)
        if (avgEyeHeight < 2.5) {
          debugLog('VIOLATION: Sleep detected!');
          playSound();
          showAlert('😴 Sleep/drowsiness detected!');
          setTimeout(() => redirectToLogin('sleep'), 2000);
          return;
        }

        setStatus({ type: 'ok', text: '✅ All good' });
        debugLog('All checks passed');
      }

      detectionIntervalRef.current = setTimeout(detectLoop, 100);
    } catch (error) {
      debugLog('Detection error: ' + error.message);
      detectionIntervalRef.current = setTimeout(detectLoop, 100);
    }
  };

  const checkGazeDirection = (landmarks, canvas) => {
    try {
      // Get eye and nose positions
      const leftEye = landmarks[39];
      const rightEye = landmarks[42];
      const nose = landmarks[30];
      const leftEyeOuter = landmarks[36];
      const rightEyeOuter = landmarks[45];
      
      // Calculate eye center
      const eyeCenterX = (leftEye.x + rightEye.x) / 2;
      const eyeCenterY = (leftEye.y + rightEye.y) / 2;
      
      // Calculate gaze direction vector
      const gazeX = nose.x - eyeCenterX;
      const gazeY = nose.y - eyeCenterY;
      
      // Calculate face width for normalization
      const faceWidth = Math.abs(rightEyeOuter.x - leftEyeOuter.x);
      
      // Normalize gaze direction
      const normalizedGazeX = gazeX / faceWidth;
      const normalizedGazeY = gazeY / faceWidth;
      
      // Define screen boundaries (more lenient)
      // User is looking at screen if gaze is within these thresholds
      const horizontalThreshold = 0.4; // Left/Right tolerance
      const verticalThreshold = 0.3;   // Up/Down tolerance
      
      // Check if gaze is within screen bounds
      const lookingAtScreen = 
        Math.abs(normalizedGazeX) < horizontalThreshold &&
        Math.abs(normalizedGazeY) < verticalThreshold;
      
      return lookingAtScreen;
    } catch (error) {
      // If calculation fails, assume looking at screen
      return true;
    }
  };

  const drawFaceTracker = (landmarks, ctx) => {
    const facePoints = [0, 16, 8, 27, 30];
    ctx.fillStyle = '#22c55e';
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 2;
    facePoints.forEach((i) => {
      const p = landmarks[i];
      ctx.beginPath();
      ctx.arc(p.x, p.y, 4, 0, Math.PI * 2);
      ctx.fill();
    });
    for (let i = 0; i < 16; i++) {
      const p1 = landmarks[i];
      const p2 = landmarks[i + 1];
      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.stroke();
    }
  };

  const drawEyeTracker = (leftEye, rightEye, nose, ctx) => {
    ctx.fillStyle = '#3b82f6';
    ctx.strokeStyle = '#60a5fa';
    ctx.lineWidth = 2;

    ctx.beginPath();
    ctx.arc(leftEye.x, leftEye.y, 6, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(rightEye.x, rightEye.y, 6, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    const gazeX = (leftEye.x + rightEye.x) / 2;
    const gazeY = (leftEye.y + rightEye.y) / 2;
    const dirX = nose.x - gazeX;
    const dirY = nose.y - gazeY;
    const length = Math.sqrt(dirX * dirX + dirY * dirY);
    const normalX = dirX / length;
    const normalY = dirY / length;

    const gazeLength = 150;
    const endX = gazeX + normalX * gazeLength;
    const endY = gazeY + normalY * gazeLength;

    const gradient = ctx.createLinearGradient(gazeX, gazeY, endX, endY);
    gradient.addColorStop(0, 'rgba(59,130,246,0.8)');
    gradient.addColorStop(1, 'rgba(59,130,246,0)');
    ctx.strokeStyle = gradient;
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(gazeX, gazeY);
    ctx.lineTo(endX, endY);
    ctx.stroke();

    ctx.fillStyle = '#fbbf24';
    ctx.beginPath();
    ctx.arc(endX, endY, 8, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 2;
    ctx.stroke();
  };

  const playSound = () => {
    const audio = new Audio('data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBSuBzvLZiTYIGGS57OihUBELTKXh8bllHAU2jdXvzn0pBSh+zPDajzsKElyx6OyrWBUIQ5zd8sFuJAUuhM/z24k2CBhku+zooVARC0yl4fG5ZRwFNo3V7859KQUofsz');
    audio.play().catch(() => {});
  };

  const showAlert = (message) => {
    alert(message);
    playSound();
  };

  const redirectToLogin = async (reason) => {
    debugLog('Redirecting to login: ' + reason);
    if (detectionIntervalRef.current) clearTimeout(detectionIntervalRef.current);
    if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
    stopCamera();
    try {
      await axios.post('http://localhost:8000/violation/', { reason });
      await axios.post('http://localhost:8000/logout/');
    } catch (error) {
      console.error('Error logging violation:', error);
    }
    window.location.href = `/?reason=${reason}`;
  };

  const handleLogout = async () => {
    debugLog('Logging out...');
    if (detectionIntervalRef.current) clearTimeout(detectionIntervalRef.current);
    if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
    stopCamera();
    try {
      await axios.post('http://localhost:8000/logout/');
    } catch (error) {
      console.error('Error logging out:', error);
    }
    onLogout();
  };

  const handleStartCamera = () => {
    setCameraStarted(true);
    startTimer();
    loadCameras();
  };

  return (
    <div className="exam-page">
      <div className="topbar">
        <button className="logout-btn" onClick={handleLogout}>
          🚪 Logout
        </button>
        <div className="time-display">
          <span>⏰</span>
          <span>{time}</span>
        </div>
        <div className="student-info">
          <span className="student-name">👤 {student.name}</span>
          <span className="reg-no">{student.regno}</span>
        </div>
      </div>

      <div className="main">
        <div className="camera-panel">
          <div className="camera-box">
            <video ref={videoRef} autoPlay muted playsInline />
            <canvas ref={canvasRef} />
          </div>

          {!cameraStarted && (
            <button className="start-camera-btn" onClick={handleStartCamera}>
              📷 Start Camera & Begin Exam
            </button>
          )}

          {cameraStarted && (
            <div className="camera-controls">
              <select
                className="camera-select"
                value={selectedCamera}
                onChange={(e) => changeCamera(e.target.value)}
              >
                {cameras.map((camera, index) => (
                  <option key={camera.deviceId} value={camera.deviceId}>
                    📷 {camera.label || `Camera ${index + 1}`}
                  </option>
                ))}
              </select>
              <div className={`status-badge status-${status.type}`}>
                <div className="dot"></div>
                <span>{status.text}</span>
              </div>
            </div>
          )}
        </div>
      </div>

      <div className="debug">{debug}</div>
    </div>
  );
};

export default ExamPage;
