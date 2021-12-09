import * as d3 from 'd3';
import { useD3 } from "../../hooks/useD3";

const ArtifactBySetpieceMainStatChart = ({data}) => {
  const ref = useD3(
    (svg) => {
      const height = 500;
      const width = 800;
      const xLabel = "Stat";
      const yLabel = "Count";
      const margin = { top: 20, right: 30, bottom: 30, left: 40 };

      const x = d3
        .scalePoint()
        .domain(data.map((d) => d.stat))
        .rangeRound([margin.left, width - margin.right])
        .padding(0.3);

      const y = d3
        .scaleLinear()
        .domain([0, d3.max(data, (d) => d.count)])
        .rangeRound([height - margin.bottom, margin.top]);

      const xAxis = (g) =>
        g.attr("transform", `translate(0,${height - margin.bottom})`).call(
          d3
            .axisBottom(x)
            .tickValues([...x.domain()])
            .tickSizeOuter(0))
          .call((g) =>
            g
              .append("text")
              .attr("x", width/2)
              .attr("y", 30)
              .attr("fill", "currentColor")
              .attr("text-anchor", "start")
              .text(xLabel)
          )
        ;

      const yAxis = (g) =>
        g
          .attr("transform", `translate(${margin.left},0)`)
          .style("color", "steelblue")
          .call(d3.axisLeft(y).ticks(5))
          .call((g) => g.select(".domain").remove())
          .call((g) =>
            g
              .append("text")
              .attr("x", -margin.left)
              .attr("y", 10)
              .attr("fill", "currentColor")
              .attr("text-anchor", "start")
              .text(data.y)
          );

      svg.select(".x-axis").call(xAxis);
      svg.select(".y-axis").call(yAxis);

      svg
        .select(".plot-area")
        .attr("fill", "steelblue")
        .selectAll(".bar")
        .data(data)
        .join("rect")
        .attr("class", "bar")
        .attr("x", (d) => x(d.stat))
        .attr("width", 40)
        .attr("transform", `translate(${-20},0)`)
        .attr("y", (d) => y(d.count))
        .attr("height", (d) => y(0) - y(d.count))

    },
    [data.length]
  )

  return(
    <svg
      ref={ref}
      style={{
        height: 500,
        width: "100%",
        marginRight: "0px",
        marginLeft: "0px",
      }}
      className="artifact-chart"
    >
      <g className="plot-area" />
      <g className="x-axis" />
      <g className="y-axis" />
    </svg>
  )
}


export default ArtifactBySetpieceMainStatChart
