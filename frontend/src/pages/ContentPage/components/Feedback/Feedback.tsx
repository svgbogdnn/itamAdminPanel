import { Container } from '@src/components/Container';
import { FilterPanel } from '@src/components/FilterPanel';
import React from 'react';
import { filterFields, reviews } from './Feedback.constants';
import { Summary } from './components/Summary';
import { Review } from './components/Review';

export const Feedback = () => {
  return (
    <Container>
      <FilterPanel fields={filterFields} />
      <Summary course='PYTHON PRO' averageRating='4.99' commentsCount='10052' />
      {reviews.map((review) => <Review key={review.id} review={review} />)}
    </Container>
  );
};
