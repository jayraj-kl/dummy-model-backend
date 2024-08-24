const express = require('express');
const exec = require('child_process').exec;
const promisify = require('util').promisify;

const app = express();
const port = 5000;
app.use(express.json());
const execPromise = promisify(exec);

async function runPythonScript() {
  try {
    const { stdout, stderr } = await execPromise(`python app.py`);
    if (stderr) {
      console.error(`stderr: ${stderr}`);
    }
    return stdout;  // Return stdout here
  } catch (error) {
    console.error(`exec error: ${error}`);
    return `Exec error: ${error}`;
  }
}


app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.post("/predict", async (req, res)  => {
  const result = await runPythonScript();
  res.send(result);
});

app.listen(port, () => {
  console.log(`Express app listening at http://localhost:${port}`);
});
