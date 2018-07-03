import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Redirect, Switch, Link} from 'react-router-dom';


const Categories = ({ match }) => (
  <div>
    <h2>Categories</h2>
    <ul>
      <li>
        <Link to={`${match.url}/rendering`}>Rendering with React</Link>
      </li>
      <li>
        <Link to={`${match.url}/components`}>Components</Link>
      </li>
      <li>
        <Link to={`${match.url}/props-v-state`}>Props v. State</Link>
      </li>
    </ul>

    <Route path={`${match.url}/:categoryId`} component={Category} />
    <Route
      exact
      path={match.url}
      render={() => <h3>Please select a category.</h3>}
    />
  </div>
);

const Category = ({ match }) => (
  <div>
    <h3>{match.params.categoryId}</h3>
  </div>
);


export default Categories;