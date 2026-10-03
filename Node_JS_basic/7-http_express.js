const express = require('express');
const fs = require('fs');

const app = express();

app.get('/', (request, response) => {
  response.type('text/plain').send('Hello Holberton School!');
});

app.get('/students', async (request, response) => {
  const lines = ['This is the list of our students'];

  try {
    const content = await fs.promises.readFile(process.argv[2], 'utf8');
    const rows = content.split(/\r?\n/).filter((row) => row.trim() !== '');
    const students = rows.slice(1);
    const fields = new Map();

    students.forEach((student) => {
      const [firstName, , , field] = student.split(',');
      if (!fields.has(field)) {
        fields.set(field, []);
      }
      fields.get(field).push(firstName);
    });

    lines.push(`Number of students: ${students.length}`);
    fields.forEach((names, field) => {
      lines.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    });
  } catch (error) {
    lines.push('Cannot load the database');
  }

  response.type('text/plain').send(lines.join('\n'));
});

app.listen(1245);

module.exports = app;
