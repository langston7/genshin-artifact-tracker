import { NavLink } from 'react-router-dom';

function SideBar({show}){

  return(
    <div className={`sidebar-container ${show ? "null" : "reveal-navbar"}`}>
      <NavLink className="sidebar-link" to='/'>Home</NavLink>
      <NavLink className="sidebar-link" to='/my-artifacts'>My Artifacts</NavLink>
      <NavLink className="sidebar-link" to='/log-artifacts'>Log Artifacts</NavLink>
      <NavLink className="sidebar-link" to='/login'>Log In</NavLink>
      <NavLink className="sidebar-link" to='/sign-up'>Sign Up</NavLink>
      <NavLink className="sidebar-link" to='/'>Log Out</NavLink>
    </div>
  )
}

export default SideBar
