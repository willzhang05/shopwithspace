import React from 'react';
import { connect } from 'react-redux';
import { HashRouter as Router, Switch, Route } from 'react-router-dom';

import { initializeApp } from './AppRouterActions';
import MapView from './MapView';

class AppRouter extends React.Component {
  componentDidMount() {
    this.props.initializeApp();
  }
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path='/' component={MapView} />
        </Switch>
      </Router>
    );
  }
}

const mapDispatchToProps = {
  initializeApp
};

export default connect(null, mapDispatchToProps)(AppRouter);
