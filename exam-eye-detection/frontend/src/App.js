import React, { useState } from 'react';
import Login from './components/Login';
import ExamPage from './components/ExamPage';
import './App.css';

function App() {
  const [student, setStudent] = useState(null);
  const [sessionId, setSessionId] = useState(null);

  const handleLogin = (studentData, sessionId) => {
    setStudent(studentData);
    setSessionId(sessionId);
  };

  const handleLogout = () => {
    setStudent(null);
    setSessionId(null);
  };

  return (
    <div className="App">
      {!student ? (
        <Login onLogin={handleLogin} />
      ) : (
        <ExamPage student={student} sessionId={sessionId} onLogout={handleLogout} />
      )}
    </div>
  );
}

export default App;
