import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Redirect, Switch, Link} from 'react-router-dom';


const Tickets = ({ match }) => (
  <div>
    <h2>Tickets</h2>
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

    <Route path={`${match.url}/:ticketId`} component={Ticket} />
    <Route
      exact
      path={match.url}
      render={() => <h3>Please select a ticket.</h3>}
    />
  </div>
);

const Ticket = ({ match }) => (
  <div>
    <h3>{match.params.ticketId}</h3>
  </div>
);


export default Tickets;