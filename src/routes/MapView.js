import React from 'react';
import { connect } from 'react-redux';
import Map from '../components/Map';
import Loader from '../components/Loader';

class MapView extends React.Component {
  render() {
    if (this.props.location.latitude && this.props.location.longitude)
      return <Map></Map>;
    return <Loader></Loader>;
  }
}

const mapStateToProps = state => {
  return {
    location: state.location
  };
};

export default connect(mapStateToProps, null)(MapView);
