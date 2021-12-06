import { useState } from "react";

function ArtifactCard({artifact}){


  const [show, setShow] = useState(true);
  const updateSetShow = (e) => {
    show ? setShow(false) : setShow(true);
  }

  return(

    <div className = "artifact-card" onClick={updateSetShow}>
      <div className = {`artifact-preview ${show ? null : "hidden"}`}>
        <img src={artifact.image} className="artifact-item artifact-thumbnail" alt="artifact"></img>
        <div>{artifact.name}</div>
        <div>{artifact.date}</div>
      </div>
      <div className = {`artifact-fullview" ${show ? "hidden" : null}`}>
        <img src={artifact.image} className="artifact-item artifact-thumbnail" alt="artifact"></img>
        <div>{artifact.name}</div>
        <div>{artifact.rarity}</div>
        <div>{artifact.date}</div>
        <div>{artifact.primary_stat} {artifact.primary_stat_value}</div>
        <div>{artifact.secondary_stat_one} {artifact.secondary_stat_one_value}</div>
        <div>{artifact.secondary_stat_two} {artifact.secondary_stat_two_value}</div>
        <div>{artifact.secondary_stat_three} {artifact.secondary_stat_three_value}</div>
        <div>{artifact.secondary_stat_four} {artifact.secondary_stat_four_value}</div>
      </div>
    </div>

  )

}


export default ArtifactCard;
