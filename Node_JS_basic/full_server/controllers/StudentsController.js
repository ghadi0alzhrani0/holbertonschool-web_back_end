import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    return readDatabase(process.argv[2])
      .then((studentsByField) => {
        const lines = ['This is the list of our students'];
        const fields = Object.keys(studentsByField)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        fields.forEach((field) => {
          const names = studentsByField[field];
          lines.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        });

        return response.type('text/plain').status(200).send(lines.join('\n'));
      })
      .catch(() => response.type('text/plain').status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      return response.type('text/plain').status(500).send('Major parameter must be CS or SWE');
    }

    return readDatabase(process.argv[2])
      .then((studentsByField) => {
        const names = studentsByField[major] || [];
        return response.type('text/plain').status(200).send(`List: ${names.join(', ')}`);
      })
      .catch(() => response.type('text/plain').status(500).send('Cannot load the database'));
  }
}

export default StudentsController;
