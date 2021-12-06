import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getOneUsersArtifacts } from "../../store/user_artifacts";
import ArtifactChart from "../ArtifactChart";

const Home = () => {

  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const artifacts = useSelector(state => Object.values(state.userArtifacts));

  const propDict = {
    'HP': 0,
    'ATK': 0,
    'DEF': 0,
    'Energy Recharge': 0,
    'Elemental Mastery': 0,
    'ATK%': 0,
    'DEF%': 0,
    'CRIT RATE': 0,
    'CRIT DMG': 0,
  };
  artifacts.forEach((art) => {
    //if(!propDict[art.primary_stat]){ propDict[art.primary_stat] = 0 }
    propDict[art.primary_stat]++;
  })

  let primary_stats = Object.keys(propDict);
  let finalDictArr = []
  primary_stats.forEach((stat) => {
    finalDictArr.push({'stat': stat, 'count': propDict[stat]})
  })


  console.log(artifacts);
  console.log(propDict);
  console.log('********');
  console.log(finalDictArr);
  useEffect(() => {
    dispatch(getOneUsersArtifacts(user?.id));
  }, [dispatch, user])

  return(
    <div className="body-inner">
      <div>Welcome to Home</div>
      <ArtifactChart data={finalDictArr}/>
    </div>
  )
}


export default Home
