const { PythonShell } = require("python-shell");
const static = require("node-static");
const http = require("http");
const socketIO = require("socket.io");
const path = require("path");

// Serve static files from 'public' folder
const fileServer = new static.Server(path.join(__dirname, "public"));

// Create HTTP server
const server = http.createServer((req, res) => {
  req
    .addListener("end", () => {
      fileServer.serve(req, res);
    })
    .resume();
});

// Enable WebSockets
const io = socketIO(server);

// On new socket connection
io.on("connection", (socket) => {
  console.log("⚡ Client connected");
  socket.emit("console_output", "[✓ Connected to server]");

  function runGame() {
    const pyshell = new PythonShell("run.py");

    // Receive input from frontend and send to Python
    socket.on("command_entered", (data) => {
      try {
        pyshell.send(data);
      } catch (err) {
        console.error("Error sending to Python:", err);
        socket.emit("console_output", `[Error] Failed to send input: ${err.toString()}`);
      }
    });

    // Receive messages from Python and send to terminal
    pyshell.on("message", (msg) => {
      socket.emit("console_output", msg.trimEnd());
    });

    // Handle errors from PythonShell
    pyshell.on("error", (err) => {
      console.error("🐍 PythonShell error:", err);
      socket.emit("console_output", `[Python Error] ${err.toString()}`);
    });

    // Python shell ends
    pyshell.on("close", () => {
      socket.emit("console_output", "\n[Game ended]");
    });

    // Clean up on client disconnect
    socket.on("disconnect", () => {
      pyshell.kill();
      console.log("🚪 Client disconnected");
    });
  }

  runGame();
});

// Start Node server
const PORT = process.env.PORT || 5000;
server.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});

// const PythonShell = require("python-shell").PythonShell;
// const static = require("node-static");
// const http = require("http");
// const socketIO = require("socket.io");
// const fs = require("fs");
// const path = require("path");

// // Server static files from 'public' folder
// const fileServer = new static.Server(path.join(__dirname, "public"));

// //Create Http server
// const server = http.createServer((req, res) => {
//   req
//     .addListener("end", () => {
//       fileServer.serve(req, res);
//     })
//     .resume();
// });

// // Enable Socket.IO on the server
// const io = socketIO(server);

// // Socket connection event
// io.on("connection", (socket) => {
//   console.log("Client connected");
//   socket.emit("console_output", "[Connected to server]");

//   //Run the Python game
//   function runGame() {
//     const pyshell = new PythonShell("run.py");

//     socket.on("command_entered", (data) => {
//       try {
//         pyshell.send(data);
//       } catch (err) {
//         console.log("Error sending to Python:", err);
//         socket.emit("console_output", `[Error] Failed to send input: ${err.toString()}`);
//       }
//     });

//     pyshell.on("message", (msg) => {
//       socket.emit("console_output", msg);
//     });

//     // catch pyhton errors and prevent full crash
//     pyshell.on("error", (err) => {
//       console.log("Error in Python:", err);
//       socket.emit("console_output", `[Python Error] ${err.toString()}`);
//     });

//     pyshell.on("close", () => {
//       socket.emit("console_output", "\n[Game ended]");
//     });

//     socket.on("disconnect", () => {
//       pyshell.kill(); // Kill Python shell
//       console.log("Client disconnected");
//     });
//   }

//   runGame();
// });

// // Start server
// const PORT = process.env.PORT || 5000;
// server.listen(PORT, () => {
//   console.log(`Server running on port ${PORT}`);
// });
