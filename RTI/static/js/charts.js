
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



let chartoptions2 = {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
                autoSkip: true,
                max: 1,
                fontFamily: 'Noto Sans KR',
                fontColor: '#fff',
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



let chartoptions3 = {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
                autoSkip: true,
                max: 3,
                fontFamily: 'Noto Sans KR',
                fontColor: '#fff',
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

let sellosschart = document.getElementById('loss-chart').getContext('2d');
let losschartdatasets = [{
    label: 'Train Loss',
    data: trainloss,
    borderWidth: 2,
    fill: true,
    backgroundColor: 'rgba(30, 183, 247, .1)',
    borderColor: 'rgba(30, 183, 247, 1)',
    pointBorderColor: 'rgba(30, 183, 247, 1)',
    pointBackgroundColor: 'rgba(30, 183, 247, 1)',
    pointHoverBackgroundColor: 'rgba(30, 183, 247, 1)',
    pointRadius: 1,
    tension: 0.3
}];

let selaccuracychart = document.getElementById('accuracy-chart').getContext('2d');
let accuracychartdatasets = [{
    label: 'Train Accuracy',
    data: trainaccuracy,
    borderWidth: 2,
    fill: true,
    backgroundColor: 'rgba(15, 236, 42, .1)',
    borderColor: 'rgba(15, 236, 42, 1)',
    pointBorderColor: 'rgba(15, 236, 42, 1)',
    pointBackgroundColor: 'rgba(15, 236, 42, 1)',
    pointHoverBackgroundColor: 'rgba(15, 236, 42, 1)',
    pointRadius: 1,
    tension: 0.3
}];
