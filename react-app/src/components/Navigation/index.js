import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import './Navigation.css';
import { useState } from "react";
import SideBar from './SideBar';

const Navigation = () => {

  const user = useSelector(state => state.session.user)
  const [show, setShow] = useState(true);
  const updateSetShow = (e) => {
    show ? setShow(false) : setShow(true);
  }

  return (
    <nav className='nav-container'>
      <div className='nav-inner'>
        <div onClick={updateSetShow}>|||</div>
        <SideBar show={show}/>
        <NavLink to='/'>Home</NavLink>
        <NavLink to='/my-artifacts'>My Artifacts</NavLink>
        <NavLink to='/log-artifacts'>Log Artifacts</NavLink>
        <NavLink to='/login'>Log In</NavLink>
        <NavLink to='/sign-up'>Sign Up</NavLink>
        <NavLink to='/'>Log Out</NavLink>
      </div>
    </nav>
  )
}



export default Navigation
