const fs = require('fs');

function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

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

  console.log(`Number of students: ${students.length}`);
  fields.forEach((names, field) => {
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  });
}

module.exports = countStudents;
