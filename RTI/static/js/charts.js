
let chartoptions = {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
                autoSkip: true,
                max: 100,
                fontFamily: 'Noto Sans KR',
                fontColor: '#fff',
                callback: function (value, index, values) {
                    return value + '%'
                }
            }
        }],
        xAxes: [{
            ticks: {
                autoSkip: true,
                max: 100,
                fontFamily: 'Noto Sans KR',
                fontColor: '#fff'
            }
        }]
    }
};

let selcpuchart = document.getElementById('cpu-chart').getContext('2d');
let cpuchartdatasets = [{
    label: 'CPU Usage',
    data: cpuper,
    borderWidth: 3,
    fill: true,
    backgroundColor: 'rgba(246, 41, 99, .1)',
    borderColor: 'rgba(246, 41, 99, 1)',
    pointBorderColor: 'rgba(246, 41, 99, 1)',
    pointBackgroundColor: 'white',
    pointHoverBackgroundColor: 'white',
    tension: 0.3
}];

var selmemorychart = document.getElementById('memory-chart').getContext('2d');
let memorychartdatasets = [{
    label: 'Memory Usage',
    data: memoryper,
    borderWidth: 3,
    fill: true,
    backgroundColor: 'rgba(15, 236, 202, .1)',
    borderColor: 'rgba(15, 236, 202, 1)',
    pointBorderColor: 'rgba(15, 236, 202, 1)',
    pointBackgroundColor: 'white',
    pointHoverBackgroundColor: 'white',
    tension: 0.3
}];

let seldiskchart = document.getElementById('disk-chart').getContext('2d');
let diskchartdatasets = [{
    label: 'Disk Usage',
    data: diskper,
    borderWidth: 3,
    fill: true,
    backgroundColor: 'rgba(236, 213, 15, .1)',
    borderColor: 'rgba(236, 213, 15, 1)',
    pointBorderColor: 'rgba(236, 213, 15, 1)',
    pointBackgroundColor: 'white',
    pointHoverBackgroundColor: 'white',
    tension: 0.3
}];