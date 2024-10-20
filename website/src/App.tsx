import './App.css'
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import Practice from './pages/Practice';
import Stats from './pages/Stats';
import { useState } from 'react';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Practice setLoggedIn={setLoggedIn} />} />
        <Route path="/stats" element={<Stats loggedIn={loggedIn} setLoggedIn={setLoggedIn} />} />
      </Routes>
    </Router>
  );
}

export default App
