const GET_USER_ARTIFACTS = 'user_artifact/getUserArtifacts';
const DELETE_USER_ARTIFACT = 'user_artifact/deleteUserArtifact';

const get_user_artifacts = (user_artifacts) => {
  return {
    type: GET_USER_ARTIFACTS,
    payload: user_artifacts,
  };
}

const delete_user_artifact = (user_artifact_id) => {
  return{
    type: DELETE_USER_ARTIFACT,
    payload: user_artifact_id
  }
}

export const getAllUsersArtifacts = () => async dispatch => {
  const response = await fetch('/api/user_artifacts/');
  const data = await response.json();
  dispatch(get_user_artifacts(data.user_artifacts));
}

export const getOneUsersArtifacts = (user_id) => async dispatch => {
  const response = await fetch(`/api/user_artifacts/${user_id}`);
  const data = await response.json();
  dispatch(get_user_artifacts(data.user_artifacts));
}

export const deleteUserArtifact = (user_artifact_id) => async dispatch => {
  const response = await fetch(`/api/user_artifacts/${user_artifact_id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
  })
  if(response.ok){
    await dispatch(delete_user_artifact(user_artifact_id))
    return null
  }
}

const userArtifactReducer = (state = {}, action) => {
  let newState;
  switch (action.type) {
    case GET_USER_ARTIFACTS:
      newState = Object.assign({}, state);
      newState = action.payload;
      return newState;
    case DELETE_USER_ARTIFACT:
      newState = Object.assign({}, state);
      delete newState[action.payload];
      return newState;
    default:
      return state;
  }
}

export default userArtifactReducer;
