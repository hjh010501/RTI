let pusher = new Pusher('4fa94fab975bd79f2408', {
    cluster: 'ap3',
    forceTLS: true
});

// Enable pusher logging - don't include this in production
Pusher.logToConsole = true;

let cpuchannel = pusher.subscribe('rti-cpu-channel');
cpuchannel.bind('cpu-perform', function (data) {
    // document.querySelector('.layout-center > h3').innerHTML += JSON.stringify(data);
    if (cpucount.length >= 20) {
        cpucount.shift()
        cpuper.shift()
    }

    cpucount.push(cpucount_number);
    cpuper.push(Math.round(data.p));
    c4.circleProgress('value', Math.round(data.p) * 0.01);
    cpucount_number++;
    cpuchart.update()
});

let memorychannel = pusher.subscribe('rti-memory-channel');
memorychannel.bind('memory-perform', function (data) {
    if (memorycount.length >= 20) {
        memorycount.shift()
        memoryper.shift()
    }

    memorycount.push(memorycount_number);
    memoryper.push(Math.round(data.mper));
    c5.circleProgress('value', Math.round(data.mper) * 0.01);
    memorycount_number++;
    memorychart.update();
    document.getElementById('memoryused').innerHTML = data.mused;
    document.getElementById('memoryunused').innerHTML = data.munused;
});

// let channel = pusher.subscribe('rti-battery-channel');
// channel.bind('battery-perform', function (data) {
//     document.querySelector('.layout-center > h2').innerHTML += JSON.stringify(data);
// });

let diskchannel = pusher.subscribe('rti-disk-channel');
diskchannel.bind('disk-perform', function (data) {
    if (diskcount.length >= 20) {
        diskcount.shift()
        diskper.shift()
    }

    diskcount.push(diskcount_number);
    diskper.push(Math.round(data.dper));
    c6.circleProgress('value', Math.round(data.dper) * 0.01);
    diskcount_number++;
    diskchart.update()
    document.getElementById('diskused').innerHTML = data.dused;
    document.getElementById('diskunused').innerHTML = data.dunused;
});

let trainchannel = pusher.subscribe('rti-train-channel');
trainchannel.bind('train-perform', function (data) {
    trainepoch.push(data.epoch);
    trainloss.push(data.loss);
    trainaccuracy.push(data.accuracy);
    if (maxloss <= data.loss) {
        maxloss = data.loss;
        chartoptions3.scales.yAxes[0].ticks.max = maxloss;
    }
    losschart.update();
    accuracychart.update();
    document.getElementById('lossvalue').innerHTML = data.loss;
    document.getElementById('accuracyvalue').innerHTML = data.accuracy;
    $('.logspanel').append("[" + data.t + "] " + data.logs + "<br>");
    $(".logspanel").scrollTop($(".logspanel")[0].scrollHeight);
});