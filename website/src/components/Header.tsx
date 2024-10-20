import FunicsLogo from '../assets/funics_logo.png';
import { useLocation } from 'react-router-dom';

export default function Header() {
  const location = useLocation();
  const home = location.pathname === '/';
  let navAway;

  if (home) {
    navAway = (
      <a href="/stats" className='navAway'>Stats</a>
    )
  } else {
    navAway = (
      <a href="/" className='navAway'>Practice</a>
    )
  }

  return (
    <header className="navHeader">
      <img src={FunicsLogo} alt="Funics Logo" className='headerLogo' />
      <div className='nav'>
        {navAway}
      </div>
    </header>
  )
}