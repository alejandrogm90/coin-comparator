async function insert_data_json() {
    const data_json = {{ month_data | safe }} ;
    ctx = document.getElementById('myChart');

    dt = [];
    for coin_element in data_json:
        dt[coin_element] = {
            label: coin_element,
            data: data_json[coin_element]
        }

    new Chart(ctx, {
        type: 'line',
        options: {
            responsive: true,
            parsing: {
                xAxisKey: 'date_part',
                yAxisKey: 'value'
            },
            legend: {
                 position: 'top',
            },
            title: {
                display: true,
                text: 'Chart.js Line Chart'
            }
        },
        data: {
            labels: data_json.map(row => row.date_part),
            datasets: dt
        },
    });
};

document.addEventListener("DOMContentLoaded", insert_data_json);