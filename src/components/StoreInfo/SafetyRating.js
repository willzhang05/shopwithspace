import React from 'react';
import { connect } from 'react-redux';

class SafetyRating extends React.Component {
  render() {
    let safetyText = '';
    switch (Math.round(this.props.obj.safety)) {
      case 5:
        safetyText = 'very safe';
        break;
      case 4:
        safetyText = 'safe';
        break;
      case 3:
        safetyText = 'caution';
        break;
      case 2:
        safetyText = 'unsafe';
        break;
      case 1:
        safetyText = 'very unsafe';
        break;
      default:
        break;
    }

    let popularity =
      'current_popularity' in this.props.obj.popular
        ? this.props.obj.popular.current_popularity
        : 'Unknown';
    let time_wait =
      'time_wait' in this.props.obj.popular
        ? this.props.obj.popular.time_wait
        : 'Unknown';
    let time_spent =
      'time_spent' in this.props.obj.popular
        ? this.props.obj.popular.time_spent
        : 'Unknown';
    return (
      <div className='safety-rating'>
        <div className={'safety-score r' + Math.round(this.props.obj.safety)}>
          <span className='safety-number'>
            {this.props.obj.safety.toFixed(1)}
          </span>
          <span className='safety-text'>{safetyText}</span>
        </div>

        <div className='safety-breakdown'>
          <h3>Safety Metrics</h3>
          <div className='row'>
            <h4>Traffic Flow</h4>
            <p>
              {(
                this.props.obj.current_speed / this.props.obj.free_flow_speed
              ).toFixed(2)}
            </p>
          </div>
          <div className='text'>
            Higher traffic flow indicates less vehicles on the road.
          </div>

          <div className='row'>
            <h4>Popularity</h4>
            <p>{popularity}</p>
          </div>
          <div className='text'>
            Higher popularity indicates more people in the store.
          </div>

          <div className='row'>
            <h4>Average Wait Time</h4>
            <p>{time_wait}</p>
          </div>
          <div className='text'>
            Lower wait time indicates less contact with people in the store.
          </div>

          <div className='row'>
            <h4>Average Time Spent</h4>
            <p>{time_spent}</p>
          </div>
          <div className='text'>
            Lower time spent indicates less people in the store.
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    current: state.current,
    obj: state.stores[state.current]
  };
};

export default connect(mapStateToProps, null)(SafetyRating);
