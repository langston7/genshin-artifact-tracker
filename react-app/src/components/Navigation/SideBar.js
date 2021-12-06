import { NavLink } from 'react-router-dom';

function SideBar(){

  return(
    <div className='sidebar-container'>
      <NavLink to='/'>Home</NavLink>
      <NavLink to='/my-artifacts'>My Artifacts</NavLink>
      <NavLink to='/log-artifacts'>Log Artifacts</NavLink>
      <NavLink to='/login'>Log In</NavLink>
      <NavLink to='/sign-up'>Sign Up</NavLink>
      <NavLink to='/'>Log Out</NavLink>
    </div>
  )
}

export default SideBar
