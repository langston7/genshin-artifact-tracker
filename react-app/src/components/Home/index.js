import * as Plot from "@observablehq/plot";
import * as d3 from 'd3';

const Home = () => {
  const alphabet = [{letter: "A", freq: 2}, {letter: "B", freq: 5}, {letter: "C", freq: 3}]

  return(
    <svg
      style={{
        height: 500,
        width: "100%",
        marginRight: "0px",
        marginLeft: "0px",

      }}
    >
      <g className="plot-area" />
      <g className="x-axis" />
      <g className="y-axis" />
    </svg>
  )
}


export default Home
