import React from 'react';
import { connect } from 'react-redux';
import GoogleMapReact from 'google-map-react';

import { getStores } from './MapActions';

import Marker from './Marker';
import CurrentMarker from './CurrentMarker';

class Map extends React.Component {
  componentDidMount() {
    this.props.getStores();
  }
  render() {
    const center = {
      lat: this.props.location.latitude,
      lng: this.props.location.longitude
    };

    return (
      <div id='map'>
        <GoogleMapReact
          bootstrapURLKeys={{ key: 'AIzaSyCl3oN8un11v0d7DGCJ9QQYEh7nf93Vu0Q' }}
          defaultCenter={center}
          defaultZoom={10}
          yesIWantToUseGoogleMapApiInternals
        >
          {this.props.stores.map((obj, index) => (
            <Marker
              key={obj.id}
              index={index}
              lat={obj.location.lat}
              lng={obj.location.lng}
              obj={obj}
            />
          ))}
          <CurrentMarker
            lat={this.props.location.latitude}
            lng={this.props.location.longitude}
          />
        </GoogleMapReact>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    location: state.location,
    stores: state.stores
  };
};

const mapDispatchToProps = {
  getStores
};

export default connect(mapStateToProps, mapDispatchToProps)(Map);
