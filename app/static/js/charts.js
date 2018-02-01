window.onload = function() {
	createChart();
}


function createChart() {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "https://api.coindesk.com/v1/bpi/historical/close", false);
	xhr.send();
	var response = JSON.parse(xhr.responseText);
	var bitcoinChart = document.getElementById("bitcoinChart").getContext('2d');
	var etheriumChart = document.getElementById("etheriumChart").getContext('2d');
	var litecoinChart = document.getElementById("litecoinChart").getContext('2d');


	var data = response.bpi,
		lables = [],
		bitcoin = [],
		etherium = [],
		litecoin = [];

	for (var property in data) {

		if (!data.hasOwnProperty(property)) {
			continue;
		}

		lables.push(property);
		bitcoin.push(data[property]);
		var precision = 10000; // 2 decimals
		etherium.push(Math.floor(Math.random() * (800 * precision - 700 * precision) + 700 * precision) / (1 * precision));
		litecoin.push(Math.floor(Math.random() * (150 * precision - 100 * precision) + 100 * precision) / (1 * precision));
	}

	var bitcoinChart = new Chart(bitcoinChart, {
		type: 'line',
		data: {
			labels: lables,
			datasets: [{
				label: 'Bitcoin',
				data: bitcoin,
				backgroundColor: [
					'rgba(54, 162, 235, 0.2)',

				],
				borderColor: [
					'rgba(54, 162, 235, 1)',

				],
				borderWidth: 1
			}]
		},
		options: {
			scales: {
				yAxes: [{
					ticks: {
						beginAtZero: true
					}
				}]
			}
		}
	});

	var etheriumChart = new Chart(etheriumChart, {
		type: 'line',
		data: {
			labels: lables,
			datasets: [{
				label: 'Etherium',
				data: etherium,
				backgroundColor: [
					'rgba(255, 206, 86, 0.2)',

				],
				borderColor: [
					'rgba(255, 206, 86, 1)',
				],
				borderWidth: 1
			}]
		},
		options: {
			scales: {
				yAxes: [{
					ticks: {
						beginAtZero: true
					}
				}]
			}
		}
	});

	var litecoinChart = new Chart(litecoinChart, {
		type: 'line',
		data: {
			labels: lables,
			datasets: [{
				label: 'Litecoin',
				data: litecoin,
				backgroundColor: [
					'rgba(255, 99, 132, 0.2)',

				],
				borderColor: [
					'rgba(255, 99, 132, 1)',
				],
				borderWidth: 1
			}]
		},
		options: {
			scales: {
				yAxes: [{
					ticks: {
						beginAtZero: true
					}
				}]
			}
		}
	});
}