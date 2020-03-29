import React from 'react';
import { connect } from 'react-redux';
import Sidebar from '../components/Sidebar';
import Map from '../components/Map';
import Loader from '../components/Loader';
import StoreInfo from '../components/StoreInfo';

class MapView extends React.Component {
  render() {
    const modal = this.props.current != null ? <StoreInfo></StoreInfo> : null;
    if (this.props.location.latitude && this.props.location.longitude)
      return (
        <div className='map-view-container'>
          <Sidebar />
          <Map></Map>
          {modal}
        </div>
      );
    return <Loader></Loader>;
  }
}

const mapStateToProps = state => {
  return {
    location: state.location,
    current: state.current
  };
};

export default connect(mapStateToProps, null)(MapView);
