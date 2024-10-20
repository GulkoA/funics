import { useNavigate } from "react-router-dom";
import Header from "../components/Header";
import { useEffect } from "react";
import ReactApexChart from "react-apexcharts";

const stuff = {
  series: [{
    name: 'Series 1',
    data: [8, 5, 3, 4, 10, 2, 8, 5, 3, 4, 10, 2],
  }],
  options: {
    // chart: {
    //   height: 35,
    //   type: 'radar',
    // },
    title: {
      text: ''
    },
    yaxis: {
      stepSize: 2
    },
    xaxis: {
      categories: ['January', 'February', 'March', 'April', 'May', '1June', '1January', '1February', '1March', '1April', '1May', '1June']
    }
  },
};

export default function Stats({ loggedIn, setLoggedIn }:
  {
    loggedIn: boolean;
    setLoggedIn: (value: boolean) => void;
  }) {

  const navigate = useNavigate();

  useEffect(() => {
    if (!loggedIn) {
      const password = window.prompt("Please enter some text:");

      if (password === "thisisthepassword") {
        setLoggedIn(true);
      } else {
        navigate('/');
      }
    }
  }, [loggedIn, navigate, setLoggedIn]);

  return loggedIn ? (
    <div className="page">
      <Header setLoggedIn={setLoggedIn} />
      <div>
        <h1>Statistics</h1>

        <ReactApexChart
          series={stuff.series}
          options={stuff.options}
          type="radar"
          height={350}
        />
      </div>
    </div>
  ) : (
    <div className="page">
      <h1 className="center">Please log in!</h1>
    </div>
  );
}