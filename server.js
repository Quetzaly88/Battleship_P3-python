const PythonShell = require("python-shell").PythonShell;
const static = require("node-static");
const http = require("http");
const socketIO = require("socket.io");
const fs = require("fs");
const path = require("path");

// Server static files from 'ppublic' folder
const fileServer = new static.Server(path.join(__dirname, "public"));

//Create Http server
const server = http.createServer((req, res) => {
  req
    .addListener("end", () => {
      fileServer.serve(req, res);
    })
    .resume();
});

// Enable Socket.IO on the server
const io = socketIO(server);

// Socket connection event
io.on("connection", (socket) => {
  console.log("Client connected");

  //Run the Python game
  function runGame() {
    const pyshell = new PythonShell("run.py");

    //when user sends input, pass it to Python
    socket.on("command_entered", (data) => {
      try {
        pyshell.send(data);
      } catch (err) {
        console.log("Error sending to Python:", err);
      }
    });

    //when Python sends output, send it to user
    pyshell.on("message", (msg) => {
      socket.emit("console_output", msg);
    });
    // End event
    pyshell.on("close", () => {
      socket.emit("console_output", "\n[Game ended]");
    });

    // Handle disconnect
    socket.on("disconnect", () => {
      pyshell.kill(); // Kill Python shell
      console.log("Client disconnected");
    });
  }

  runGame();
});

// Start server
const PORT = process.env.PORT || 5000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
