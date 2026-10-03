class AppController {
  static getHomepage(request, response) {
    return response.status(200).type('text/plain').send('Hello Holberton School!');
  }
}

export default AppController;
