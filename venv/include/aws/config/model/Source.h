﻿/**
 * Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0.
 */

#pragma once
#include <aws/config/ConfigService_EXPORTS.h>
#include <aws/config/model/Owner.h>
#include <aws/core/utils/memory/stl/AWSString.h>
#include <aws/core/utils/memory/stl/AWSVector.h>
#include <aws/config/model/SourceDetail.h>
#include <utility>

namespace Aws
{
namespace Utils
{
namespace Json
{
  class JsonValue;
  class JsonView;
} // namespace Json
} // namespace Utils
namespace ConfigService
{
namespace Model
{

  /**
   * <p>Provides the Config rule owner (Amazon Web Services or customer), the rule
   * identifier, and the events that trigger the evaluation of your Amazon Web
   * Services resources.</p><p><h3>See Also:</h3>   <a
   * href="http://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/Source">AWS API
   * Reference</a></p>
   */
  class AWS_CONFIGSERVICE_API Source
  {
  public:
    Source();
    Source(Aws::Utils::Json::JsonView jsonValue);
    Source& operator=(Aws::Utils::Json::JsonView jsonValue);
    Aws::Utils::Json::JsonValue Jsonize() const;


    /**
     * <p>Indicates whether Amazon Web Services or the customer owns and manages the
     * Config rule.</p>
     */
    inline const Owner& GetOwner() const{ return m_owner; }

    /**
     * <p>Indicates whether Amazon Web Services or the customer owns and manages the
     * Config rule.</p>
     */
    inline bool OwnerHasBeenSet() const { return m_ownerHasBeenSet; }

    /**
     * <p>Indicates whether Amazon Web Services or the customer owns and manages the
     * Config rule.</p>
     */
    inline void SetOwner(const Owner& value) { m_ownerHasBeenSet = true; m_owner = value; }

    /**
     * <p>Indicates whether Amazon Web Services or the customer owns and manages the
     * Config rule.</p>
     */
    inline void SetOwner(Owner&& value) { m_ownerHasBeenSet = true; m_owner = std::move(value); }

    /**
     * <p>Indicates whether Amazon Web Services or the customer owns and manages the
     * Config rule.</p>
     */
    inline Source& WithOwner(const Owner& value) { SetOwner(value); return *this;}

    /**
     * <p>Indicates whether Amazon Web Services or the customer owns and manages the
     * Config rule.</p>
     */
    inline Source& WithOwner(Owner&& value) { SetOwner(std::move(value)); return *this;}


    /**
     * <p>For Config managed rules, a predefined identifier from a list. For example,
     * <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule,
     * see <a
     * href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Using
     * Config managed rules</a>.</p> <p>For custom rules, the identifier is the Amazon
     * Resource Name (ARN) of the rule's Lambda function, such as
     * <code>arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name</code>.</p>
     */
    inline const Aws::String& GetSourceIdentifier() const{ return m_sourceIdentifier; }

    /**
     * <p>For Config managed rules, a predefined identifier from a list. For example,
     * <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule,
     * see <a
     * href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Using
     * Config managed rules</a>.</p> <p>For custom rules, the identifier is the Amazon
     * Resource Name (ARN) of the rule's Lambda function, such as
     * <code>arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name</code>.</p>
     */
    inline bool SourceIdentifierHasBeenSet() const { return m_sourceIdentifierHasBeenSet; }

    /**
     * <p>For Config managed rules, a predefined identifier from a list. For example,
     * <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule,
     * see <a
     * href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Using
     * Config managed rules</a>.</p> <p>For custom rules, the identifier is the Amazon
     * Resource Name (ARN) of the rule's Lambda function, such as
     * <code>arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name</code>.</p>
     */
    inline void SetSourceIdentifier(const Aws::String& value) { m_sourceIdentifierHasBeenSet = true; m_sourceIdentifier = value; }

    /**
     * <p>For Config managed rules, a predefined identifier from a list. For example,
     * <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule,
     * see <a
     * href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Using
     * Config managed rules</a>.</p> <p>For custom rules, the identifier is the Amazon
     * Resource Name (ARN) of the rule's Lambda function, such as
     * <code>arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name</code>.</p>
     */
    inline void SetSourceIdentifier(Aws::String&& value) { m_sourceIdentifierHasBeenSet = true; m_sourceIdentifier = std::move(value); }

    /**
     * <p>For Config managed rules, a predefined identifier from a list. For example,
     * <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule,
     * see <a
     * href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Using
     * Config managed rules</a>.</p> <p>For custom rules, the identifier is the Amazon
     * Resource Name (ARN) of the rule's Lambda function, such as
     * <code>arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name</code>.</p>
     */
    inline void SetSourceIdentifier(const char* value) { m_sourceIdentifierHasBeenSet = true; m_sourceIdentifier.assign(value); }

    /**
     * <p>For Config managed rules, a predefined identifier from a list. For example,
     * <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule,
     * see <a
     * href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Using
     * Config managed rules</a>.</p> <p>For custom rules, the identifier is the Amazon
     * Resource Name (ARN) of the rule's Lambda function, such as
     * <code>arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name</code>.</p>
     */
    inline Source& WithSourceIdentifier(const Aws::String& value) { SetSourceIdentifier(value); return *this;}

    /**
     * <p>For Config managed rules, a predefined identifier from a list. For example,
     * <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule,
     * see <a
     * href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Using
     * Config managed rules</a>.</p> <p>For custom rules, the identifier is the Amazon
     * Resource Name (ARN) of the rule's Lambda function, such as
     * <code>arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name</code>.</p>
     */
    inline Source& WithSourceIdentifier(Aws::String&& value) { SetSourceIdentifier(std::move(value)); return *this;}

    /**
     * <p>For Config managed rules, a predefined identifier from a list. For example,
     * <code>IAM_PASSWORD_POLICY</code> is a managed rule. To reference a managed rule,
     * see <a
     * href="https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html">Using
     * Config managed rules</a>.</p> <p>For custom rules, the identifier is the Amazon
     * Resource Name (ARN) of the rule's Lambda function, such as
     * <code>arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name</code>.</p>
     */
    inline Source& WithSourceIdentifier(const char* value) { SetSourceIdentifier(value); return *this;}


    /**
     * <p>Provides the source and type of the event that causes Config to evaluate your
     * Amazon Web Services resources.</p>
     */
    inline const Aws::Vector<SourceDetail>& GetSourceDetails() const{ return m_sourceDetails; }

    /**
     * <p>Provides the source and type of the event that causes Config to evaluate your
     * Amazon Web Services resources.</p>
     */
    inline bool SourceDetailsHasBeenSet() const { return m_sourceDetailsHasBeenSet; }

    /**
     * <p>Provides the source and type of the event that causes Config to evaluate your
     * Amazon Web Services resources.</p>
     */
    inline void SetSourceDetails(const Aws::Vector<SourceDetail>& value) { m_sourceDetailsHasBeenSet = true; m_sourceDetails = value; }

    /**
     * <p>Provides the source and type of the event that causes Config to evaluate your
     * Amazon Web Services resources.</p>
     */
    inline void SetSourceDetails(Aws::Vector<SourceDetail>&& value) { m_sourceDetailsHasBeenSet = true; m_sourceDetails = std::move(value); }

    /**
     * <p>Provides the source and type of the event that causes Config to evaluate your
     * Amazon Web Services resources.</p>
     */
    inline Source& WithSourceDetails(const Aws::Vector<SourceDetail>& value) { SetSourceDetails(value); return *this;}

    /**
     * <p>Provides the source and type of the event that causes Config to evaluate your
     * Amazon Web Services resources.</p>
     */
    inline Source& WithSourceDetails(Aws::Vector<SourceDetail>&& value) { SetSourceDetails(std::move(value)); return *this;}

    /**
     * <p>Provides the source and type of the event that causes Config to evaluate your
     * Amazon Web Services resources.</p>
     */
    inline Source& AddSourceDetails(const SourceDetail& value) { m_sourceDetailsHasBeenSet = true; m_sourceDetails.push_back(value); return *this; }

    /**
     * <p>Provides the source and type of the event that causes Config to evaluate your
     * Amazon Web Services resources.</p>
     */
    inline Source& AddSourceDetails(SourceDetail&& value) { m_sourceDetailsHasBeenSet = true; m_sourceDetails.push_back(std::move(value)); return *this; }

  private:

    Owner m_owner;
    bool m_ownerHasBeenSet;

    Aws::String m_sourceIdentifier;
    bool m_sourceIdentifierHasBeenSet;

    Aws::Vector<SourceDetail> m_sourceDetails;
    bool m_sourceDetailsHasBeenSet;
  };

} // namespace Model
} // namespace ConfigService
} // namespace Aws
