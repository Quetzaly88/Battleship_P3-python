const { PythonShell } = require("python-shell");
const static = require("node-static");
const http = require("http");
const socketIO = require("socket.io");
const path = require("path");

const fileServer = new static.Server(path.join(__dirname, "public"));

const server = http.createServer((req, res) => {
  req
    .addListener("end", () => {
      fileServer.serve(req, res);
    })
    .resume();
});

const io = socketIO(server);

io.on("connection", (socket) => {
  console.log("Client connected");
  // socket.emit("console_output", "[✓ Connected to server]");

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
      console.error("PythonShell error:", err);
      socket.emit("console_output", `[Python Error] ${err.toString()}`);
    });

    // Python shell ends
    pyshell.on("close", () => {
      socket.emit("console_output", "\n[Game ended]");
    });

    // Clean up on client disconnect
    socket.on("disconnect", () => {
      pyshell.kill();
      console.log("Client disconnected");
    });
  }

  runGame();
});

// Start Node server
const PORT = process.env.PORT || 5000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
