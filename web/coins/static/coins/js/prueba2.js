
async function get_json_data() {
    const response = await fetch("http://127.0.0.1:8000/get_json_month/2022-01-01/");
    data_json = await response.json();
    console.log(data_json);
    return data_json;
}

async function insert_data_json() {
  const data = [
    { year: 2010, count: 10 },
    { year: 2011, count: 20 },
    { year: 2012, count: 15 },
    { year: 2013, count: 25 },
    { year: 2014, count: 22 },
    { year: 2015, count: 30 },
    { year: 2016, count: 28 },
  ];

  ctx = document.getElementById('myChart');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.map(row => row.year),
      datasets: [
        {
          label: 'Acquisitions by year',
          data: data.map(row => row.count)
        }
      ]
    }
  });
};

function ready2() {
    insert_data_json();
};

document.addEventListener("DOMContentLoaded", ready2);