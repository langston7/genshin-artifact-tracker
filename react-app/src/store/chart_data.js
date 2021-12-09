const GET_CHART_DATA1 = 'chartData/getChartData1';
const GET_CHART_DATA2 = 'chartData/getChartData2';

const get_chart_data1 = (chart_data) => {
  return {
    type: GET_CHART_DATA1,
    payload: chart_data,
  };
}

const get_chart_data2 = (chart_data) => {
  return {
    type: GET_CHART_DATA2,
    payload: chart_data,
  };
}

export const getDataForMainStatChart = (user_id) => async dispatch => {
  const response = await fetch(`/api/user_artifacts/${user_id}/dataForMainStatChart`);
  const data = await response.json();
  dispatch(get_chart_data1(data.data));
}

export const getDataForSetpieceMainStatChart = (user_id) => async dispatch => {
  const response = await fetch(`/api/user_artifacts/${user_id}/dataForSetpieceMainStatChart`);
  const data = await response.json();
  dispatch(get_chart_data2(data));
}


const chartDataReducer = (state = {}, action) => {
  let newState;
  switch (action.type) {
    case GET_CHART_DATA1:
      newState = Object.assign({}, state);
      newState['0'] = action.payload;
      return newState;
    case GET_CHART_DATA2:
      newState = Object.assign({}, state);
      newState['1'] = action.payload;
      return newState;
    default:
      return state;
  }
}


export default chartDataReducer;
