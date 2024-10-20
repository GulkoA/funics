import FunicsLogo from '../assets/funics_logo.png';
import { Link, useLocation } from 'react-router-dom';
import SensorDoorOutlinedIcon from '@mui/icons-material/SensorDoorOutlined';

export default function Header({ setLoggedIn }: { setLoggedIn: (value: boolean) => void }) {
  const location = useLocation();
  const practice = location.pathname === '/';
  let navAway;

  if (practice) {
    navAway = (
      <Link to="/stats" className='navAway' onClick={() => {
        setLoggedIn(false);
      }}>
        <SensorDoorOutlinedIcon className='navAway' style={{ fontSize: "40" }} />
      </Link>
    )
  } else {
    navAway = (
      <Link to="/" className='navAway'>Practice</Link>
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