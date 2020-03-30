import React from 'react';
import { connect } from 'react-redux';
import { hoverBar } from './PopularTimesActions';
import moment from 'moment';

class PopularTimes extends React.Component {
  hoverBar(hour, day) {
    this.props.hoverBar(hour, day);
  }
  render() {
    let populartimes = null;
    let d = new Date();
    let currentDay = (d.getDay() + 6) % 7;
    let day =
      this.props.currentPopularDay != null
        ? this.props.currentPopularDay
        : currentDay;
    let hour =
      this.props.currentPopularTime != null
        ? this.props.currentPopularTime
        : d.getHours();
    const list = this.props.obj.popular.populartimes;
    const poptimes = list.map((obj, day) => {
      let i = (day + currentDay) % 7;
      return (
        <div className='pop-time' key={day}>
          <div className='day'>{list[i].name}</div>
          <div className='bars'>
            {list[i].data.map((obj, index) => (
              <div
                key={index}
                className={'bar r' + Math.round((100 - obj) / 25 + 1)}
                style={{ height: Math.max(100 - obj, 10) + '%' }}
                onMouseEnter={() => this.hoverBar(index, i)}
                onMouseLeave={() => this.hoverBar(null, null)}
              >
                <div className='tooltip'>{Math.max(100 - obj, 1) + '%'}</div>
              </div>
            ))}
          </div>
          <div className='time'>
            <span>12:00 AM</span>
            <span>12:00 PM</span>
          </div>
        </div>
      );
    });
    let time = moment().hour(hour);
    time.day(day + 1);

    populartimes = (
      <div className='container'>
        <h4>Safe Times</h4>
        <div className='pop-times-container'>
          <div className='modal-popular-times'>{poptimes}</div>
          <div className='popular-rating'>
            <span className='popularity'>
              {Math.max(100 - list[day].data[hour], 1)}% safe
            </span>
            <span className='day'>{time.format('dddd')}</span>
            <span className='time'>{time.format('h A')}</span>
          </div>
        </div>
      </div>
    );
    return populartimes;
  }
}

const mapStateToProps = state => {
  return {
    current: state.current,
    currentPopularTime: state.currentPopularTime,
    currentPopularDay: state.currentPopularDay,
    obj: state.stores[state.current]
  };
};

const mapDispatchToProps = {
  hoverBar
};

export default connect(mapStateToProps, mapDispatchToProps)(PopularTimes);
