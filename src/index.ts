import express from 'express';
import { exec } from 'child_process';
import { promisify } from 'util';

const app = express();
app.use(express.json());
const port = process.env.PORT || 3000;
const execPromise = promisify(exec);

async function runPythonScript(movieTitle: string) {
  try {
    const { stdout, stderr } = await execPromise(`python scripts.py "${movieTitle}"`);
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
  res.json({
    message: 'Hello, TypeScript with Express!'
  });
});

app.post('/', async (req, res) => {  // Mark the handler as async
  const title = req.body.title;
  const reco = await runPythonScript(title);  // Use await to wait for the result

  // Process the recommendation message
  const lines = reco.split('\r\n').filter(line => line.trim() !== ''); // Split and filter out empty lines
  const movieObjects = lines.slice(1).map(movie => ({ movie })); // Skip the first line and map to objects

  res.json({
    movies: movieObjects
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
