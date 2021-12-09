import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getDataForMainStatChart, getDataForSetpieceMainStatChart } from "../../store/chart_data";
import { getOneUsersArtifacts } from "../../store/user_artifacts";
import ArtifactByMainStatChart from "../ArtifactByMainStatChart";
import ArtifactBySetpieceMainStatChart from "../ArtifactBySetpieceMainStatChart";

const Home = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const dataForMainStatChart = useSelector(state => state.chartData[0]);
  const dataForSetpieceMainStatChart = useSelector(state => state.chartData[1]);
  console.log(dataForSetpieceMainStatChart)
  const [currentSetpiece, setCurrentSetpiece] = useState('Sands of Eon');

  //<ArtifactBySetpieceMainStatChart data={dataForSetpieceMainStatChart}/>

  useEffect(() => {
    dispatch(getOneUsersArtifacts(user?.id));
    dispatch(getDataForMainStatChart(user?.id));
    dispatch(getDataForSetpieceMainStatChart(user?.id));
  }, [dispatch, user])

  const updateCurrentSetpiece = (e) =>{
    setCurrentSetpiece(e.target.value);
  }

  return(
    <div className="body-inner">
      <div>Welcome to Home</div>
      {dataForMainStatChart ? <ArtifactByMainStatChart data={dataForMainStatChart}/> : null}
      <div>Select which Artifact slot you'd like to view data on.</div>
      <select onChange={updateCurrentSetpiece}>
        <option value='Sands of Eon'>Sands of Eon</option>
        <option value='Goblet of Eonothem'>Goblet of Eonothem</option>
        <option value='Circlet of Logos'>Circlet of Logos</option>
      </select>
      {dataForSetpieceMainStatChart ? <ArtifactBySetpieceMainStatChart data={dataForSetpieceMainStatChart[currentSetpiece]}/> : null}
    </div>
  )
}


export default Home
