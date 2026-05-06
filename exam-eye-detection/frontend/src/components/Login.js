import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Login.css';

const Login = ({ onLogin }) => {
  const [isSignUp, setIsSignUp] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    phone: '',
    email: '',
    college: '',
    regno: '',
    password: '',
    confirmPassword: ''
  });
  const [warning, setWarning] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const reason = params.get('reason');
    if (reason) {
      const reasons = {
        face: '⚠️ Camera blocked or face hidden',
        multiple: '⚠️ Multiple persons detected',
        sleep: '⚠️ Sleep/drowsiness detected',
        lookdown: '⚠️ Looked down >2 seconds',
        outofbox: '⚠️ Head turned outside camera',
        headturn: '⚠️ Head turned outside camera',
        blocked: '⚠️ Camera blocked or hidden',
        gaze_away: '⚠️ Looking away from screen (3 warnings)'
      };
      setWarning(reasons[reason] || '⚠️ Rule violation');
    }
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (isSignUp && formData.password !== formData.confirmPassword) {
      alert('Passwords do not match!');
      return;
    }
    
    setLoading(true);
    try {
      const endpoint = isSignUp ? 'http://localhost:8000/signup/' : 'http://localhost:8000/login/';
      const payload = isSignUp 
        ? {
            name: formData.name,
            phone: formData.phone,
            email: formData.email,
            college: formData.college,
            regno: formData.regno,
            password: formData.password
          }
        : {
            regno: formData.regno,
            password: formData.password
          };
      
      const response = await axios.post(endpoint, payload);
      if (response.data.success) {
        onLogin(response.data.student, response.data.session_id);
      } else {
        alert(response.data.error || 'Authentication failed');
      }
    } catch (error) {
      console.error('Authentication error:', error);
      alert(error.response?.data?.error || 'Server error. Please make sure the backend server is running on port 8000.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-page">
      <div className="login-card">
        <div className="login-header">
          <h1>VizionX</h1>
          <p className="subtitle">{isSignUp ? 'Create your account' : 'Enter your details to begin the exam'}</p>
        </div>

        {warning && (
          <div className="warning-box">
            {warning}
          </div>
        )}

        <form className="login-form" onSubmit={handleSubmit}>
          {!isSignUp ? (
            // Login Form
            <>
              <div className="form-field">
                <label>🪪 Register Number</label>
                <input
                  type="text"
                  name="regno"
                  value={formData.regno}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-field">
                <label>🔒 Password</label>
                <input
                  type="password"
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                  required
                />
              </div>

              <button className="btn" type="submit" id="submitBtn">🚀 Login to Exam</button>

              <p className="signup-prompt">
                <span onClick={() => window.location.href='/forgot-password/'} style={{cursor:'pointer',textDecoration:'underline'}}>Forgot Password?</span>
              </p>

              <p className="signup-prompt">
                Don't have an account? <span onClick={() => setIsSignUp(true)}>Create new one</span>
              </p>
            </>
          ) : (
            // Sign Up Form
            <>
              <div className="form-field">
                <label>👤 Full Name</label>
                <input
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-field">
                <label>🪪 Register Number</label>
                <input
                  type="text"
                  name="regno"
                  value={formData.regno}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="form-field">
                <label>📱 Phone Number</label>
                <input
                  type="tel"
                  name="phone"
                  value={formData.phone}
                  onChange={handleChange}
                  pattern="[0-9]{10}"
                  required
                />
              </div>

              <div className="form-field">
                <label>🔒 Create Password</label>
                <input
                  type="password"
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                  minLength="6"
                  required
                />
              </div>

              <div className="form-field">
                <label>🔒 Confirm Password</label>
                <input
                  type="password"
                  name="confirmPassword"
                  value={formData.confirmPassword}
                  onChange={handleChange}
                  minLength="6"
                  required
                />
              </div>

              <div className="form-field">
                <label>🏫 College Name</label>
                <input
                  type="text"
                  name="college"
                  value={formData.college}
                  onChange={handleChange}
                  required
                />
              </div>

              <button className="btn-primary" type="submit" disabled={loading}>
                {loading ? '⏳ Loading...' : '📝 Sign Up & Start Exam'}
              </button>

              <button
                className="btn-secondary"
                type="button"
                onClick={() => setIsSignUp(false)}
              >
                🔙 Back to Login
              </button>
            </>
          )}
        </form>

        <p className="note">
          📷 Your webcam will be monitored throughout the exam.<br />
          Any violation will immediately end your session.
        </p>
      </div>
    </div>
  );
};

export default Login;
