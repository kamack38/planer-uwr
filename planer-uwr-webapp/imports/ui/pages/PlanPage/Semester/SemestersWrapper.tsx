import React from 'react';

import { Course } from '../../../../api/courses';
import { Semester } from '../../../../api/plans';
import { SemesterWrapper } from './SemesterWrapper';

interface SemestersWrapperProps {
  courses: Record<string, Course>;
  semesters: Semester[];
}

function sumHoursByType(arr: string[]) {
  const sums = {
    'ćw.': 0,
    'wyk.': 0,
    'inne': 0
  };

  arr.forEach(item => {
    // Extract the number and the type string using regex
    const match = item.match(/(\d+)\s*\((.+)\)/);
    if (match) {
      const value = parseInt(match[1], 10);
      const label = match[2];

      if (label === 'wyk.') {
        sums['wyk.'] += value;
      } else if (label === 'ćw.' || label === 'ćw-prac.' || label === 'prac.') {
        sums['ćw.'] += value;
      } else {
        sums['inne'] += value;
      }
    }
  });

  // Convert sums object back to array format
  return sums;
}

export const SemestersWrapper = ({
  courses,
  semesters,
}: SemestersWrapperProps) => {
  let sum = 0;

  return (
    <div className='semesters-wrapper'>
      {semesters.map((semester, index) => {
        if (semester.isGap) {
          return (
            <SemesterWrapper
              courses={courses}
              semester={semester}
              key={index}
              ects={0}
              totalEcts={0}
            />
          );
        }

        const partialSum = semester.courses
          .map((course) => {
            if (courses[course.id] === undefined) {
              console.log("UNDEFINED")
              console.log({ courses, course })
            }
            return course.source === 'custom'
              ? 0 /* TOOD custom courses  */
              : courses[course.id]?.ects ?? 0
          }
          )
          .reduce((a, b) => a + b, 0);
        sum += partialSum;
        const hours = sumHoursByType(semester.courses.flatMap((course) => {
          if (courses[course.id] === undefined) {
            console.log("UNDEFINED")
            console.log({ courses, course })
          }
          return course.source === 'custom'
            ? [] /* TOOD custom courses  */
            : courses[course.id]?.hours ?? []
        }));

        return (
          <SemesterWrapper
            courses={courses}
            semester={semester}
            key={index}
            ects={partialSum}
            totalEcts={sum}
            hours={hours}
          />
        );
      })}
    </div>
  );
};
