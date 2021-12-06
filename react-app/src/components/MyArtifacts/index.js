import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getOneUsersArtifacts } from "../../store/user_artifacts";
import ArtifactCard from "./ArtifactCard";
import './MyArtifacts.css'

const MyArtifacts = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const artifacts = useSelector(state => Object.values(state.userArtifacts));

  useEffect(() => {
    dispatch(getOneUsersArtifacts(user?.id));
  }, [dispatch, user])

  return(
    <div className="body-inner">
      <div>My Artifacts</div>
      {artifacts?.map((artifact) =>
        <ArtifactCard artifact={artifact}/>
      )}
    </div>

  )
}


export default MyArtifacts
