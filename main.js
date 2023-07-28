'use strict';

const express = require('express');
const http = require('http');
const CryptoJS = require('crypto-js');
const mysql = require('mysql');

// Constants
const PORT = 8889;
const HOST = '0.0.0.0';

// App
const app = express();
app.use(express.json());

var ip_host = "192.168.250.130";
var path_host = "/auth";
var port_host = "8080";

var db_config = {
        host: "127.0.0.1",
        port: "3306",
        user: "username",
        password: "password",
        database: "dbname"
    };

function handleDisconnect() {
    connection = mysql.createConnection(db_config);
    connection.connect(function(err) {
        if (err) {
            console.log('error when connecting to db:', err);
            setTimeout(handleDisconnect, 2000);
        }
    });
    connection.on('error', function(err) {
        console.log('db error', err);
        if (err.code === 'PROTOCOL_CONNECTION_LOST') {
            handleDisconnect();
        } else {
            throw err;
        }
    });
}

handleDisconnect();

function logs(endpoint,session,req_channel,req_host,res_host,res_channel){
	var datetime = new Date().toString().slice(0, 23);
	console.log('info','=================================endpoint=================================');
	console.log('info',endpoint);
	console.log('info','=================================datetime=================================');
	console.log('info',datetime);
	console.log('info','=================================session=================================');
	console.log('info',session);
	console.log('info','===============================req_channel================================');
	console.log('info',req_channel);
	console.log('info','=================================req_host=================================');
	console.log('info',req_host);
	console.log('info','=================================res_host=================================');
	console.log('info',res_host);
	console.log('info','===============================res_channel================================');
	console.log('info',res_channel);
	console.log('info','==========================================================================');
}

function sessionHeader(id, nama){
	var id = id_agen;
	var username = username;
	var no_rekening = 'no_rekening';
	var nama = 'nama';
	var no_hp = 'no_hp';
	var email = 'email';

	var header = Buffer.from('{"alg": "HS256","typ": "JWT"}').toString('base64');
	header = header.replace(/=+$/, '');
	header = header.replace(/\+/g, '-');
	header = header.replace(/\//g, '_');

	var payload = {
		iss: username,
		sub: id_agen,
		name: nama_agen,
		iat: Math.floor(new Date().getTime() / 1000)
	};

	var payload64 = Buffer.from(JSON.stringify(payload)).toString('base64');
	payload64 = payload64.replace(/=+$/, '');
	payload64 = payload64.replace(/\+/g, '-');
	payload64 = payload64.replace(/\//g, '_');

	var signature = CryptoJS.HmacSHA256(header + '.' + payload64, password).toString(CryptoJS.enc.Base64);
	signature = signature.replace(/=+$/, '');
	signature = signature.replace(/\+/g, '-');
	signature = signature.replace(/\//g, '_');

	var value = header + '.' + payload64 + '.' + signature
	return value;
}

app.get('/', (req, res) => {
    res.send('Hello World');
});

app.post('/consume-api', function(req, res, body) {
	var session = sessionHeader(req.body.id, req.body.name);
	var data = JSON.stringify({
		"username": "BNIAG50299",
		"password": "Ipybni06!",
		"id_api": "web"
	});
	
	const options = {
		host: ip_host,
		port: 8080,
		path: path_host,
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'Content-Length': data.length,
			'Session': session
		}
	}

	var httpResponse = '';
	var output = new Object;
	
	const reqHost = http.request(options, resHost => {
		console.log('statusCode: ' + resHost.statusCode);
		
		resHost.on('data', d => {
			//process.stdout.write(d);
			httpResponse += d;
		});
		
		resHost.on('end', () => {
			output = JSON.parse(httpResponse);
			console.log('session: ' + JSON.parse(httpResponse).session);
			res.send(output);
			//logs('/product',session,req.body,data,httpResponse,output);
		});
	});

	reqHost.on('error', error => {
		console.error(error)
	});

	reqHost.write(data);
	reqHost.end();
});

app.post('/db-connect', function(req, res, body) {
	var query = "select * from user;"
	connection.query(query, function(err, rows) {
	if (err) {
		output = {
			code: err.message,
			message: err.message,
			data: null
		}
	} else {
		output = rows;
	}
	res.send(output);
});
});

app.listen(PORT, HOST);
console.log('====================================================');
console.log(`Jalan nih servicenya http://${HOST}:${PORT}`);
console.log('====================================================');