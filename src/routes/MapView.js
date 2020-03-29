import React from 'react';
import { connect } from 'react-redux';
import StoreResults from '../components/StoreResults';
import Map from '../components/Map';
import Loader from '../components/Loader';

class MapView extends React.Component {
  render() {
    if (this.props.location.latitude && this.props.location.longitude)
      return (
        <div className='map-view-container'>
          <StoreResults />
          <Map></Map>
        </div>
      );
    return <Loader></Loader>;
  }
}

const mapStateToProps = state => {
  return {
    location: state.location
  };
};

export default connect(mapStateToProps, null)(MapView);
