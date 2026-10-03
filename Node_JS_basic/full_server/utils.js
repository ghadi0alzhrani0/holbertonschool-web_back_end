import fs from 'fs';

export default function readDatabase(path) {
  return fs.promises.readFile(path, 'utf8').then((content) => {
    const rows = content.split(/\r?\n/).filter((row) => row.trim() !== '');
    const studentsByField = {};

    rows.slice(1).forEach((row) => {
      const [firstName, , , field] = row.split(',');
      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstName);
    });

    return studentsByField;
  });
}
