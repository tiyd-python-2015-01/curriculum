# Create an Instagram clone with Ember


## Description

The assignment is to create an Instagram "clone" using Ember and Parse's REST API, that replicates a particular set of features.

## Objectives

### Learning Objectives

After completing this assignment, you should…

* Understand basic session persistence using tokens (instead of cookies).
* Understand basic concepts of model relationships.

### Performance Objectives

After completing this assignment, you be able to effectively use

* localStorage to store auth tokens
* Ember controller dependencies
* Asynchronous Ember initializers
* Use permissions to effectively prevent users from altering each other's data
* Structure your data to allow for efficient queries from your database. 


## Details

### Deliverables

* A repo containing at least:
  * `gulpfile.js`
  * `package.json`
  * `bower.json`
  * `main.js`
  * `index.html`
  * `test/main.js`
  * `test/index.html`
  * `test/bower.json`
  
### Requirements

* Passing unit tests
* No JSHint warnings or errors


## Normal Mode

Users should be able to:

* create an account and log in
* post photos
* go to another user's url and see their photos

## Hard Mode

In addition to the requirements from **Normal Mode**, users should be able to:

* like photos
* comment on photos
* follow users.
* add filters to their photos

## Notes

This project can be be done in a bare-bones manner rather quickly, but a though polish of the features and styles will be time-consuming. Make sure you're intimately aquainted with the documentation for the datastore you're using, and any libraries or database adapters you're using to interact with it.

## Additional Resources

* Read [A tutorial for a similar project using Parse and iOS](https://www.parse.com/tutorials/anypic). Feel free to rely heavily on the data model and architecture explained in the tutorial.
* Check out [http://fabricjs.com/image-filters/]()
* Check out [http://evanw.github.io/glfx.js/demo/#lensBlur]()
* Read [http://emberjs.com/guides/controllers/dependencies-between-controllers/]()
* Read [http://nerdyworm.com/blog/2013/04/03/ember-initializers/]()
