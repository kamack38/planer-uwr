import { useTracker } from 'meteor/react-meteor-data';
import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { DraggableProvided } from 'react-beautiful-dnd';
import { Tag, Button, Drawer, Classes } from '@blueprintjs/core';
import { Popover2, Tooltip2 } from '@blueprintjs/popover2';
import { Courses } from '../../../api/courses';
import { CourseEntry } from '../../../api/plans';
import { courseTypeById, getTextColor } from '../../../utils';
import CourseTypeTag from './CourseTypeTag';
import CourseEffectTag from './CourseEffectTag';

interface CourseWrapperProps {
  course: CourseEntry;
  provided?: DraggableProvided;
}

export const CourseWrapper = React.memo(({
  course: { id },
  provided,
}: CourseWrapperProps) => {
  const course = useTracker(() => {
    return Courses.findOne({ id });
  }, [id]);

  if (!course) {
    return (
      <div
        ref={provided?.innerRef}
        {...provided?.draggableProps}
        {...provided?.dragHandleProps}
      ></div>
    );
  }

  const source = course.source === 'courses' ? course.semester : 'Oferta';
  const ectsPercent = course.ects > 10 ? 10 : course.ects * 10;

  const [isDescriptionOpen, setIsDescriptionOpen] = useState(false);

  return (
    <div
      ref={provided?.innerRef}
      {...provided?.draggableProps}
      {...provided?.dragHandleProps}
      className={`course-wrapper ${provided ? '' : 'course-wrapper-clone'}`}
    >
      <div className="course-wrapper-inner">
        <Button
          icon="info-sign"
          className="course-info-button"
          minimal
          onClick={() => {setIsDescriptionOpen(true)}}
        />

        <Drawer
          isOpen={isDescriptionOpen}
          title="Course Description"
          icon="info-sign"
          onClose={() => setIsDescriptionOpen(false)}
          size="50%"
        >
          <div className={Classes.DRAWER_BODY}>
            <div className={Classes.DIALOG_BODY}>
              <ReactMarkdown>{course.description}</ReactMarkdown>
            </div>
          </div>
          <div className={Classes.DRAWER_FOOTER}>
            <a href={`https://zapisy.ii.uni.wroc.pl${course.url}`} target="_blank">Open source</a>
          </div>
        </Drawer>

        <div className="course-title">{course.name}</div>
        <div>
          <CourseTypeTag courseType={courseTypeById[course.courseType]} />
          <Tag
            className="ects-tag"
            style={{
              backgroundColor: `hsl(0, 0%, ${ectsPercent * 0.7 + 15}%)`,
              color: getTextColor([
                ectsPercent * 2.55,
                ectsPercent * 2.55,
                ectsPercent * 2.55,
              ]),
            }}
          >
            {course.ects} ECTS
          </Tag>
          {course.exam ? (
            <Popover2>
              <Tooltip2
                content="Przedmiot kończy się egzaminem"
                position="bottom"
                hoverOpenDelay={300}
              >
                <Tag
                  className="ects-tag"
                  style={{
                    backgroundColor: "darkred",
                    color: "white",
                  }}
                >
                  EG
                </Tag>
              </Tooltip2>
            </Popover2>
          ) : null}
          <Tag className="source-tag">{source}</Tag>
          <CourseEffectTag effects={course.effects} />
          {course.owner === 96 ? (
            <div style={{ float: 'right' }}>
              <Popover2>
                <Tooltip2
                  content="Przedmiot Cahira"
                  position="bottom"
                  hoverOpenDelay={300}
                >
                  <img
                    src="https://github.com/cahirwpz.png"
                    style={{ borderRadius: 4 }}
                    width={22}
                    height={22}
                  />
                </Tooltip2>
              </Popover2>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
});
