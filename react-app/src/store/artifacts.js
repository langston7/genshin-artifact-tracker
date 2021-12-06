const GET_ARTIFACTS = 'artifact/getArtifacts';

const get_artifacts = (artifacts) => {
  return {
    type: GET_ARTIFACTS,
    payload: artifacts,
  };
}

export const getArtifacts = () => async dispatch => {
  const response = await fetch('/api/artifacts/');
  const data = await response.json();
  dispatch(get_artifacts(data.artifacts));
}

const artifactReducer = (state = {}, action) => {
  let newState;
  switch (action.type) {
    case GET_ARTIFACTS:
      newState = Object.assign({}, state);
      newState = action.payload;
      return newState;
    default:
      return state;
  }
}

export default artifactReducer;
