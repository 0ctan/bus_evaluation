
   const MongoClient = require("mongodb").MongoClient;
   // 接続先DB
   const url = "mongodb://localhost:27017/bus_location";

   MongoClient.connect(url, function(err, db) {
       if (err) throw err;
       var dbo = db.db("bus_location");
       dbo.collection("keiiku_A").find().sort({_id:-1}).limit(1).toArray(function(err, result) {
         if (err) throw err;
         console.log(result);
         db.close();
       });
     });
