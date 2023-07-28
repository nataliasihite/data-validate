"use strict";

const express = require("express");
const xmlparser = require("express-xml-bodyparser");
require('log-timestamp')(function() { return '' + new Date().toLocaleString('en', {timeZone: 'Asia/Jakarta'}) + ' INFO %s' });

// Constants
const PORT = 8888;
const HOST = "0.0.0.0";

// App
const app = express();
app.use(express.json());
app.use(express.urlencoded());
app.use(xmlparser());

app.get("/", (req, res) => {
  res.send("Hello World");
});

var soapResults = "";
var reffNum = new Date().toISOString().slice(0, 23).replace(/-/g, "").replace("T", "").replace(/:/g, "").replace(".", "");
var transactionDate = new Date().toISOString().slice(0, 10);

app.post("/CoreServiceJSON", function (req, res, body) {
	console.log("========================================================================");
	console.log("REQUEST");
	console.log(req.body);
	
	var output = new Object();
	output = { "systemId": "AGENT", "customHeader": null, "type": "CustomerDetail", "coreJournal": "695350", "content": { "flag": "A1", "jenisNasabah": "01", "namaNasabah": "NAMA SAYA", "gelar": "99", "titleCode": "99", "accountCurrency": "IDR", "tempatLahir": "solo", "tglLahir": "1994-02-01", "alamatId": "SOLO", "rt": "012", "rw": "9KO", "perum": "TAJAKARTAPUSAT", "kelurahan": "Gondangdia", "kecamatan": "Menteng/Kousat", "kodePos": "10350", "jalan2": "SOLO", "rt2": "012", "rw2": "9KO", "perum2": "TAJAKARTAPUSAT", "kelurahan2": "Gondangdia", "kecamatan2": "Menteng/Kousat", "kodePos2": "10350", "telpRumah": "99999999", "telpKantor": "99999999", "fax": "99999999", "email": "", "npwp": "NOT FOUND", "wargaCode": "ID", "jenisId": "0001", "tempatId": "LAKU PANDAI", "noId": "1234567890123456", "tglTerbit": "", "tglHabis": "2021-02-01", "sumberInfo": "", "maidenName": "LAKU PANDAI", "maritalIndikator": "S", "jumlahAnak": "00", "religiCode": "1", "educationCode": "03", "jobCode": "01", "namaPerusahaan": "", "alamatPerusahaan": "", "postCodePerusahaan": "", "startJobDate": "0", "gaji": "03", "namaAlias": "NAMA", "frekuensiGaji": "M", "gajiLain": "000000000000000", "handPhone": "081081081081" }, "fault": null };
	
	console.log("RESPONSE");
	console.log(output);
	console.log("========================================================================");
	res.send(output);
});

app.listen(PORT, HOST);
console.log("========================================================================");
console.log("                .      .                     .                  .       ");
console.log(",-. . ,-,-. . . |  ,-. |- ,-. ,-.    ,-. . . | , ,-.    ,-. . . | , ,-. ");
console.log("`-. | | | | | | |  ,-| |  | | |      `-. | | |<  ,-|    `-. | | |<  ,-| ");
console.log("`-' ' ' ' ' `-^ `' `-^ `' `-' '      `-' `-^ ' ` `-^    `-' `-^ ' ` `-^ ");
console.log("                                                                        ");
console.log(`Jalan nih servicenya http://${HOST}:${PORT}`);
console.log(`BNI - Simulator Suka Suka`);
console.log("========================================================================");
