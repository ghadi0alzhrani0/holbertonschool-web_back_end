const http = require('http');
const fs = require('fs');

const app = http.createServer(async (request, response) => {
  response.setHeader('Content-Type', 'text/plain');

  if (request.url === '/') {
    response.end('Hello Holberton School!');
    return;
  }

  if (request.url === '/students') {
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

    response.end(lines.join('\n'));
    return;
  }

  response.statusCode = 404;
  response.end('Not Found');
});

app.listen(1245);

module.exports = app;
