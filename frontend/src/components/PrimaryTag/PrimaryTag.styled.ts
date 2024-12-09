import styled from "styled-components";

export const Container = styled.div<{ $bgColor: string }>`
  width: 180px;
  padding: 10px;
  border-radius: 100px;
  background-color: ${({ $bgColor }) => $bgColor};
  font-family: Nunito Sans;
  font-weight: 700;
  font-size: 12px;
  line-height: 1.33;
`;
