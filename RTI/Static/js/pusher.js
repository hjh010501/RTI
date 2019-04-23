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
        console.log(cpucount);
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
        console.log(memorycount);
    }

    memorycount.push(memorycount_number);
    memoryper.push(Math.round(data.mper));
    c5.circleProgress('value', Math.round(data.mper) * 0.01);
    memorycount_number++;
    memorychart.update()

});

// let channel = pusher.subscribe('rti-battery-channel');
// channel.bind('battery-perform', function (data) {
//     document.querySelector('.layout-center > h2').innerHTML += JSON.stringify(data);
// });

let channel = pusher.subscribe('rti-disk-channel');
channel.bind('disk-perform', function (data) {
    if (diskcount.length >= 60) {
        diskcount.shift()
        diskper.shift()
        console.log(memorycount);
    }

    diskcount.push(diskcount_number);
    diskper.push(Math.round(data.dper));
    c6.circleProgress('value', Math.round(data.dper) * 0.01);
    diskcount_number++;
    diskchart.update()
});